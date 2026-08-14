# Adding and editing persistent data in your app

**Framework**: SwiftData

Create a data entry form for collecting and changing data managed by SwiftData.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- Xcode 15.0+

#### Overview

Adding and editing data are fundamental features of data-driven apps, but how an app provides these features is unique to the app. This sample shows one approach, which is to use a data-entry form with SwiftData that lets someone add, edit, and store data about animals.

##### Define the Data Model

Before SwiftData can store data from your app, the app must define the data model that represents the data. SwiftData uses model classes to construct the schema of the data model. For example, the sample app stores data about animals, and groups those animals into categories. To define the schema for this data model, the sample defines two model classes: `Animal` and `AnimalCategory`.

The `Animal` model class stores information about an animal, like its name and diet. To persist instances of `Animal`, the class definition applies the [`Model()`](model().md) macro. This macro generates code at compile time that ensures the class conforms to the [`PersistentModel`](persistentmodel.md) protocol and makes it possible for SwiftData to save animal data to a model container.

```swift
import SwiftData

@Model
final class Animal {
    var name: String
    var diet: Diet
    var category: AnimalCategory?
    
    init(name: String, diet: Diet) {
        self.name = name
        self.diet = diet
    }
}
```

The `AnimalCategory` model class stores information about an animal category, such as mammal or reptile. As with `Animal`, the `AnimalCategory` definition applies the [`Model()`](model().md) macro to ensure the class conforms to [`PersistentModel`](persistentmodel.md) and to save the animal category data to a model container.

```swift
import SwiftData

@Model
final class AnimalCategory {
    @Attribute(.unique) var name: String
    // `.cascade` tells SwiftData to delete all animals contained in the 
    // category when deleting it.
    @Relationship(deleteRule: .cascade, inverse: \Animal.category)
    var animals = [Animal]()
    
    init(name: String) {
        self.name = name
    }
}
```

The model class also has two properties:

- **`name`**: The name of the category. Each category name must be unique across all animal categories. To ensure this uniqueness, the model class applies the [`Attribute(_:originalName:hashModifier:)`](attribute(_:originalname:hashmodifier:).md) macro to the property with the option [`unique`](schema/attribute/option/unique.md). This option ensures a property’s value is unique across all models of the same type. For a complete list of options, see [`Schema.Attribute.Option`](schema/attribute/option.md).
- **`animal`**: The list of animals contained in the category. The model class applies the [`Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)`](relationship(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:).md) macro to this property to form a relationship between the model classes `AnimalCategory` and `Animal`. To learn more about the relationship, see [`Defining data relationships with enumerations and model classes`](defining-data-relationships-with-enumerations-and-model-classes.md).

##### Design the Data Editor

When deciding how people add and edit data in your app, consider the user experience. The sample app, for instance, lets someone add and edit information about animals using a custom data entry view, named `AnimalEditor`.

**iOS**:

![A screenshot of the sample app running in iOS, showing the animal editor. The editor displays horizontally a cancel button, followed by the title Add Animal, followed by a save button that appears along the top of the editor. Below that is a name field with the placeholder text Name. Below the name field is the category field the label Category, followed by a picker with the label Select a category. Below the Category field is the Diet field with the label Diet and a picker with the label Herbivore.](/images/com.apple.SwiftData/Adding-and-editing-persistent-data-02@2x.png)

**iPadOS**:

![A screenshot of the sample app running in iPadOS, showing the animal editor with sample app in the background. The editor displays horizontally a cancel button, followed by the title Add Animal, followed by a save button that appears along the top of the editor. Below that is a name field with the placeholder text Name. Below the name field is the category field the label Category, followed by a picker with the label Select a category. Below the Category field is the Diet field with the label Diet and a picker with the label Herbivore.](/images/com.apple.SwiftData/Adding-and-editing-persistent-data-03@2x.png)

**macOS**:

![A screenshot of the sample app running in macOS, showing the animal editor with the main window of the sample app in the background. The editor displays the label name next to a text field that shows the text Red kangaroo. Below the name label is a label with the text category, followed by a picker showing mammal as the selected item. Below the category label is a label with the text Diet, followed by a picker showing Herbivore as the selected item. Below these fields is a horizontal line, and below the line are two buttons displayed horizontally, cancel and save.](/images/com.apple.SwiftData/Adding-and-editing-persistent-data-01@2x.png)

**tvOS**:

![A screenshot of the sample app running in tvOS, showing the animal editor. The editor displays horizontally a cancel button, followed by the title Edit Animal, followed by a save button that appears along the top of the editor. Below that is a highlighted text field that displays the text Red kangaroo. Below the text field is a picker with the label Category and Mammal as the selected item. Below the category picker is another picker with the label Diet and Herbivore as the selected item.](/images/com.apple.SwiftData/Adding-and-editing-persistent-data-04@2x.png)

The design of `AnimalEditor` allows the app to use the same view for both adding new animals and editing existing ones. To provide this behavior, the editor declares the `animal` property as an optional `Animal` type. If `animal` is `nil`, a person using the editor is adding an animal; otherwise, the person is editing an existing animal. The editor makes the intention obvious by determining the title of the editor based on the value of `animal` in a computed property.

```swift
struct AnimalEditor: View {
    let animal: Animal?
    
    private var editorTitle: String {
        animal == nil ? "Add Animal" : "Edit Animal"
    }
    // ...
}
```

To enable editing the values of a new or existing animal, the editor defines state variables for each editable value. These state variables store the data that a person enters into the editor, separating what they enter from the data stored in `animal`. This separation ensures that SwiftData doesn’t save changes that a person makes until they’re ready to save those changes. This also gives them an opportunity to discard any changes they may have made to the data in the editor.

```swift
@State private var name = ""
@State private var selectedDiet = Animal.Diet.herbivorous
@State private var selectedCategory: AnimalCategory?

var body: some View {
    NavigationStack {
        Form {
            TextField("Name", text: $name)
            
            Picker("Category", selection: $selectedCategory) {
                Text("Select a category").tag(nil as AnimalCategory?)
                ForEach(categories) { category in
                    Text(category.name).tag(category as AnimalCategory?)
                }
            }
            
            Picker("Diet", selection: $selectedDiet) {
                ForEach(Animal.Diet.allCases, id: \.self) { diet in
                    Text(diet.rawValue).tag(diet)
                }
            }
        }
    }
}
```

The sample app takes this approach because it uses the autosave feature from SwiftData. The autosave feature automatically saves data changes made to model class instances, such as `animal`, instead of relying on the app to make explicit calls to the model context [`save()`](modelcontext/save().md) method. For more information about autosave, see [`autosaveEnabled`](modelcontext/autosaveenabled.md).

Finally, to make the purpose of the editor clear to the person using it, `AnimalEditor` uses the `editorTitle` computed property to displays the title in the [`principal`](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/principal) item section of the toolbar:

```swift
.toolbar {
    ToolbarItem(placement: .principal) {
        Text(editorTitle)
    }
}
```

##### Set Default Values

The `AnimalEditor` view declares its state variables with default values for a new animal, setting `name` to an empty string, `selectedDiet` to `herbivorous`, and leaving `selectedCategory` as `nil`. But the editor also supports editing an existing animal.

If someone edits an animal, the editor needs to show the values of the animal to edit, not the default values for the new animal. The view stores the animal to edit in the `animal` property. To show the current values of that animal, the editor applies the [`onAppear(perform:)`](https://developer.apple.com/documentation/swiftui/view/onappear(perform:)) modifier and copies the editable values from `animal` to the state variables:

```swift
.onAppear {
    if let animal {
        // Edit the incoming animal.
        name = animal.name
        selectedDiet = animal.diet
        selectedCategory = animal.category
    }
}
```

##### Save the Data Changes

To allow a person to save the changes they made in the editor, the editor provides a Save button in the toolbar:

```swift
ToolbarItem(placement: .confirmationAction) {
    Button("Save") {
        withAnimation {
            save()
            dismiss()
        }
    }
}
```

When a person clicks the Save button, it calls the editor’s `save` method. If the person is editing an existing animal, `save` copies the values from the state variables to the instance of `Animal`. This directly updates the data that SwiftData manages, and because the app uses the autosave feature, SwiftData automatically saves the changes without calling the model context [`save()`](modelcontext/save().md) method.

```swift
private func save() {
    if let animal {
        // Edit the animal.
        animal.name = name
        animal.diet = selectedDiet
        animal.category = selectedCategory
    } else {
        // Add an animal.
        // ...
    }
}
```

When adding a new animal, the `save` function creates a new `Animal` instance, initializing it with the name and diet from the state variables. Then it sets the category and inserts the animal into the model context by calling the model context [`insert(_:)`](modelcontext/insert(_:).md) method:

```swift
private func save() {
    if let animal {
        // Edit the animal.
        // ...
    } else {
        // Add an animal.
        let newAnimal = Animal(name: name, diet: selectedDiet)
        newAnimal.category = selectedCategory
        modelContext.insert(newAnimal)
    }
}
```

After saving the data, the Save button’s action closes the editor by calling [`dismiss`](https://developer.apple.com/documentation/swiftui/environmentvalues/dismiss).

> **Note**: The `AnimalEditor` view retrieves the model context from the view’s environment by creating a reference to the context with `@Environment(\.modelContext) private var modelContext`. For more information, see [`modelContext`](https://developer.apple.com/documentation/swiftui/environmentvalues/modelcontext).

##### Discard the Data Changes

To discard changes that someone made, the editor provides a Cancel button in the toolbar:

```swift
ToolbarItem(placement: .cancellationAction) {
    Button("Cancel", role: .cancel) {
        dismiss()
    }
}
```

When a person clicks the Cancel button, the editor discards any changes made to the data by calling [`dismiss`](https://developer.apple.com/documentation/swiftui/environmentvalues/dismiss) in the button’s action. This closes the editor without saving the changes.

## See Also

- [Preserving your app’s model data across launches](preserving-your-apps-model-data-across-launches.md)
  Describe your model classes to SwiftData using the framework’s macros, and store instances of those models so they exist beyond the app’s runtime.
- [Adopting SwiftData for a Core Data app](../coredata/adopting-swiftdata-for-a-core-data-app.md)
  Persist data in your app intuitively with the Swift native persistence framework.
- [SwiftData updates](../updates/swiftdata.md)
  Learn about important changes to SwiftData.
- [Adopting inheritance in SwiftData](adopting-inheritance-in-swiftdata.md)
  Add flexibility to your models using class inheritance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/adding-and-editing-persistent-data-in-your-app)*