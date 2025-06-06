# Understanding the navigation stack

**Framework**: Swiftui

Learn about the navigation stack, links, and how to manage navigation types in your app’s structure.

#### Overview

A [`NavigationStack`](navigationstack.md) is a container for your app’s navigation structure. Use a navigation stack to present a stack of views over a root view.

A `NavigationStack` exposes its state to your app with the path parameter of its initializer. To create a navigation stack with a path that you can control or track views on the navigation stack, use a [`NavigationPath`](navigationpath.md) or a [`Binding`](binding.md) to a [`RandomAccessCollection`](https://developer.apple.com/documentation/Swift/RandomAccessCollection) and [`RangeReplaceableCollection`](https://developer.apple.com/documentation/Swift/RangeReplaceableCollection) that contains [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable) elements.

A `NavigationPath` is a type-erased collection on which you can store a heterogenous list of data. For homogenous data, use an [`Array`](https://developer.apple.com/documentation/Swift/Array) instead. Because `NavigationPath` is type-erased, it can represent different types of data that correspond to a view in the navigation stack.

> 💡 **Tip**: Avoid using model types as elements of a navigation path. Make sure the elements of navigation paths are lightweight, and don’t use them as a mode of transport for data models.

Another element of the navigation stack is the , which encapsulates the views people can navigate to within your app.

You can present destinations on a `NavigationStack` using:

> **Note**: Value-destination and view-destination links don’t describe the visible stack directly; instead, they refer to the data added to the path.

##### Present View Destination Links

You can push a view onto a `NavigationStack` using `NavigationLink(destination:label:)`. With this initializer, you specify both a label—displayed on the link itself—and a destination—displayed when someone taps the link.

Enclose a [`NavigationLink`](navigationlink.md) in a navigation structure higher up in the view-hierarchy—an ancestor view, for example. If this condition isn’t met, the link typically appears as disabled.

Below is an example with two links inside a `NavigationStack`:

```swift
struct DestinationView: View {
    var body: some View {
        NavigationStack {
            NavigationLink {
                ColorDetail(color: .mint, text: "Mint")
            } label: {
                Text("Mint")
            }
            
            NavigationLink {
                ColorDetail(color: .red, text: "Red")
            } label: {
                Text("Red")
            }
        }
    }
}

struct ColorDetail: View {
    var color: Color
    var text: String

    var body: some View {
        VStack {
            Text(text)
            color
         }
    }
}
```

In this example, tapping the label titled “Mint” pushes a `ColorDetail(color: .mint, text: "Mint")` view onto the navigation stack. The navigation stack contents are the root view (the `NavigationLink` itself) at depth `0`, and `ColorDetail(color: .mint, text: "Mint")`  at depth `1`.

When you use [`init(destination:label:)`](navigationlink/init(destination:label:).md), note that:

- SwiftUI tracks the navigation state and the content of the navigation path; however, there are no stateful hooks for your app that indicate when a view has been pushed.
- Its state can’t be restored programmatically.

Use the stateful navigation techniques described in [`Manage navigation state and compose links`](understanding-the-composition-of-navigation-stack#Manage-navigation-state-and-compose-links.md) to track when a navigation link triggers, instead of [`onAppear(perform:)`](view/onappear(perform:).md) or [`task(priority:_:)`](view/task(priority:_:).md).

Use a [`navigationDestination(isPresented:destination:)`](view/navigationdestination(ispresented:destination:).md) modifier to navigate programmatically by providing a binding to a `Boolean` value. For example, you can programmatically push `ColorDetail` view onto the stack:

```swift
struct DestinationView: View { 
    @State private var showDetails = false
    var favoriteColor: Color
    
    NavigationStack {
        VStack {
            Circle()
                .fill(favoriteColor)
            Button("Show details") {
                showDetails = true
            }
        }
        .navigationDestination(isPresented: $showDetails) {
            ColorDetail(color: favoriteColor, text: color.description)
        }
    }
}
```

Use this approach when you want to navigate based on toggling state rather than by people’s interaction, or when your app presents a one-off destination with a different data type than the homogenous path of the navigation stack.

##### Present Value Destination Links

When you add data to the navigation path, SwiftUI maps the data type to a view, then pushes it onto the navigation stack when someone taps the link. To describe the view the stack displays, use the [`navigationDestination(for:destination:)`](view/navigationdestination(for:destination:).md) view modifier inside a `NavigationStack`.

The following example implements `DestinationView` as a series of navigation links:

```swift
NavigationStack {
    List {
        NavigationLink("Mint", value: Color.mint)
        NavigationLink("Red", value: Color.red)
    }
    .navigationDestination(for: Color.self) { color in
        ColorDetail(color: color, text: color.description)
    }
}
```

In the example above, SwiftUI uses the value type—in this case, `Color`—to determine the appropriate navigation destination. With value-based navigation, you can define a variety of possible destinations for a single stack When someone taps “Mint”, SwiftUI pushes `ColorDetail` view with a value `.mint` onto the stack.

Value-based navigation shines in scenarios with mixed destination types. You can extend your app to handle recipe-related content in addition to colors:

```swift
struct ValueView: View {
    private var recipes: [Recipe] = [.applePie, .chocolateCake]
    
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Mint", value: Color.mint)
                NavigationLink("Red", value: Color.red)
                ForEach(recipes) { recipe in
                    NavigationLink(recipe.description, value: recipe)
                }
            }
            .navigationDestination(for: Color.self) { color in
                ColorDetail(color: color, text: color.description)
            }
            .navigationDestination(for: Recipe.self) { recipe in
                RecipeDetailView(recipe: recipe)
            }
        }
    }
}

struct RecipeDetailView: View {
    var recipe: Recipe
    
    var body: some View {
        Text(recipe.description)
    }
}

enum Recipe: Identifiable, Hashable, Codable {
    case applePie
    case chocolateCake
    
    var id: Self { self }
    
    var description: String {
        switch self {
        case .applePie:
            return "Apple Pie"
        case .chocolateCake:
            return "Chocolate Cake"
        }
    }
}
```

In this example, the `NavigationStack` supports two destination types: `Color` for colors, and `Recipe` for recipes. SwiftUI determines the correct destination view based on the data type of the value from the navigation link.

Use [`navigationDestination(item:destination:)`](view/navigationdestination(item:destination:).md) when you need to navigate to a view based on the presence of an item. When the item binding is non-nil, SwiftUI passes the value into the destination closure and pushes the view onto the stack. For example:

```swift
struct ContentView: View {
    private var recipes: [Recipe] = [.applePie, .chocolateCake]
    @State private var selectedRecipe: Recipe?
    
    var body: some View {
        NavigationStack {
            List(recipes, selection: $selectedRecipe) { recipe in
                NavigationLink(recipe.description, value: recipe)
            }
            .navigationDestination(item: $selectedRecipe) { recipe in
                RecipeDetailView(recipe: recipe)
            }
        }
    }
}
```

When a person taps a recipe, `selectedRecipe` value updates and SwiftUI pushes `RecipeDetailView(recipe: recipe)` onto the navigation stack. You can pop the view off the stack by setting `selectedRecipe` back to nil.

##### Manage Navigation State and Compose Links

By default, a navigation stack manages state to keep track of the views on the stack. However, your app can share control of the state by initializing the stack with a binding to a collection of data values that you create.

Use [`init(path:root:)`](navigationstack/init(path:root:).md), which takes a binding to a `NavigationPath` argument, when you want to observe the navigation state for this stack.

The `NavigationPath` data type is a heterogeneous collection type that accepts any `Hashable` values. You can add to the path by calling [`append(_:)`](navigationpath/append(_:).md) or when people tap value-destination links such as [`init(value:label:)`](navigationlink/init(value:label:).md).

When you push a value onto the stack using [`init(_:value:)`](navigationlink/init(_:value:).md), you append the value to the path, as shown below:

```swift
struct ContentView: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            List {
                NavigationLink("Mint", value: Color.mint)
                NavigationLink("Red", value: Color.red)
            }
            .navigationDestination(for: Color.self) { color in
                ColorDetail(color: color)
            }
        }
    }
}
```

In this example, when someone activates a link, SwiftUI adds the corresponding value, such as `Color.mint`, to `path`. SwiftUI uses the [`State`](state.md) property called `path` to mange the state of the navigation stack.

[`init(path:root:)`](navigationstack/init(path:root:).md) also provides an initializer in which the path parameter takes a [`Binding`](binding.md) to a `RandomAccessCollection` and a `RangeReplaceableCollection` argument. You can store the path as a property in an object that leverages the [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) macro data type, and use property observers such as `willSet` and `didSet` or the [`onChange(of:initial:_:)`](view/onchange(of:initial:_:).md) modifier to respond to changes when the value-destination link triggers.

In this case, the navigation path is a homogenous collection type that accepts a standard type, such as `Array`, or a custom data type as shown below:

```swift
@Observable
class NavigationManager {
    var path: [Color] = [] {
        willSet {
            print("will set to \(newValue)")
        }
        
        didSet {
            print("didSet to \(path)")
        }
    }
}

struct ContentView: View {
    @State private var navigationManager = NavigationManager()

    var body: some View {
        NavigationStack(path: $navigationManager.path) {
            List {
                NavigationLink("Mint", value: Color.mint)
                NavigationLink("Red", value: Color.red)
            }
            .navigationDestination(for: Color.self) { color in
                ColorDetail(color: color, text: color.description)
            }
        }
    }
}
```

In the example above, the `willSet` and `didSet` property observers track when a navigation link triggers.

You can also use the reference to `path` variable to perform programmatic navigation. For example, you can pop a view off the stack:

```swift
@Observable
class NavigationManager {
    var path: [Color] = [] {
        willSet {
            print("will set to \(newValue)")
        }
        
        didSet {
            print("didSet to \(path)")
        }
    }
    
    @discardableResult
    func navigateBack() -> Color? {
        path.popLast()
    }
}
```

Use a standard type when your stack displays views that rely on a single type of data, and `NavigationPath` when you need to present multiple data types in a single stack, as in the following example:

```swift
struct ValueView: View {
    @State private var path = NavigationPath()
    
    var body: some View {
        NavigationStack(path: $path) {
            List {
                NavigationLink("Mint", value: Color.mint)
                NavigationLink("Red", value: Color.red)
                NavigationLink("Apple Pie", value: Recipe.applePie)
                NavigationLink("Chocolate Cake", value: Recipe.chocolateCake)
            }
            .navigationDestination(for: Color.self) { color in
                ColorDetail(color: color)
            }
            .navigationDestination(for: Recipe.self) { recipe in
                RecipeDetailView(recipe: recipe)
            }
        }
    }
}
```

> **Note**: Both value- and view-destination links ultimately push a user-visible view onto the stack. However, pushed value-destinations are reflected in the stack’s `path` `Binding` (if provided), while pushed view-destinations aren’t.

When composed together, the navigation APIs allow you to use both styles of links, depending on what works best.

Here, when someone taps on the link “View Mint Color”, SwiftUI pushes the value-based destination link onto the stack, followed by a view-destination link:

```swift
struct ContentView: View {
    @State private var navigationManager = NavigationManager()

    var body: some View {
        NavigationStack(path: $navigationManager.path) {
            NavigationLink("View Mint Color", value: Color.mint)
                .navigationDestination(for: Color.self) { color in
                    NavigationLink("Push Recipe View") {
                        RecipeDetailView(recipe: .applePie)
                    }
                }
        }
    }
}
```

After the code in this example runs, and someone clicks each `NavigationLink`, the navigation stack builds up with three views:

SwiftUI keeps track of the entire navigation path. The underlying data structure looks like the following example:

```swift
Root → [Color.mint] → [RecipeDetailView]
```

Conceptually, SwiftUI stacks view-based destinations on top of the value-based destinations in the stack’s navigation path. For example, the code below replaces `RecipeDetailView` from the above example with a `NavigationLink`:

```swift
struct ContentView: View {
    @State private var navigationManager = NavigationManager()

    var body: some View {
        NavigationStack(path: $navigationManager.path) {
            NavigationLink("View Mint Color", value: Color.mint)
                .navigationDestination(for: Color.self) { color in
                    NavigationLink("Push Recipe View") {
                        NavigationLink("Push another view", value: Color.pink)
                    }
                }
        }
    }
}
```

When you run the revised example, the view-destination link is still on the top of the stack.

If you use a heterogenous or homogeneous path on the stack, you may observe changes to the navigation path over time, as shown below:

```swift
@Observable
class NavigationManager {
    var path: [Color] = [] {
        didSet {
            print("didSet to \(path)")
        }
    }
}

struct ContentView: View {
    @State private var navigationManager = NavigationManager()

    var body: some View {
        NavigationStack(path: $navigationManager.path) {
            NavigationLink("View Mint Color", value: Color.mint)
                .navigationDestination(for: Color.self) { color in
                    NavigationLink("Push Recipe View") {
                        RecipeDetailView(recipe: .applePie)
                    }
                }
        }
    }
}
```

When someone navigates through the app, it prints the following logs:

```swift
New path: []
New Path: [Color.mint]
```

The logs print because view-destination navigation links don’t cause any state changes that your app can observe. If you attempt to push a value while a view-destination link is on the stack, SwiftUI pops all view destinations and pushes the value’s destination onto the stack.

##### Restore State for Navigation Paths

State restoration for a navigation path enables you restore your interface to the previous interaction point during a subsequent launch, providing continuity for people using your app.

In iOS, state restoration is especially important at the window or scene level, because windows come and go frequently. For this reason, it’s important to think about state restoration for navigation path in the same way you handle restoring your app’s state at the window or scene level. See [`Restoring Your App’s State with SwiftUI`](restoring_your_app_s_state_with_swiftui.md) to learn about storing scene data.

Using `Codable`, you can manually persist and load the navigation stack path in one of two ways, depending on whether the path data type is homogeneous or heterogeneous. Store a homogenous path as in the following example:

```swift
@Observable
class NavigationManager {
    var path: [Recipe] = [] {
        didSet {
            save()
        }
    }
    
    /// The URL for the JSON file that stores the navigation path.
    private static var dataURL: URL {
        .documentsDirectory.appending(path: "NavigationPath.json")
    }
    
    init() {
        do {
            // Load the data model from the 'NavigationPath' data file found in the Documents directory.
            let path = try load(url: NavigationManager.dataURL)
            self.path = path
        } catch {
            // Handle error.
        }
    }
    
    func save() {
        let encoder = JSONEncoder()
        do {
            let data = try encoder.encode(path)
            try data.write(to: NavigationManager.dataURL)
        } catch {
            // Handle error.
        }
    }
    
    /// Load the navigation path from a previously saved state.
    func load(url: URL) throws -> [Recipe] {
        let data = try Data(contentsOf: url, options: .mappedIfSafe)
        let decoder = JSONDecoder()
        return try decoder.decode([Recipe].self, from: data)
    }
}

struct ContentView: View {
    @State private var navigationManager = NavigationManager()

    var body: some View {
        NavigationStack(path: $navigationManager.path) {
            List {
                NavigationLink("Mint", value: Color.mint)
                NavigationLink("Red", value: Color.red)
                NavigationLink("Apple Pie", value: Recipe.applePie)
                NavigationLink("Chocolate Cake", value: Recipe.chocolateCake)
            }
            .navigationDestination(for: Color.self) { color in
                ColorDetail(color: color, text: color.description)
            }
            .navigationDestination(for: Recipe.self) { recipe in
                RecipeDetailView(recipe: recipe)
            }
        }
    }
}
```

In the above example, when the `path` changes, `didSet` property observer triggers and the `save` function is called. The function saves the new path to disk so it can be restored when the app initializes `NavigationManager`.

Store a heterogeneous path using `NavigationPath`, as shown in the following example:

```swift
@Observable
class NavigationManager {
    var path = NavigationPath() {
        didSet {
            save()
        }
    }
    
    /// The URL for the JSON file that stores the navigation path.
    private static var dataURL: URL {
        .documentsDirectory.appending(path: "NavigationPath.json")
    }
    
    init() {
        do {
            // Load the data model from the 'NavigationPath' data file found in the Documents directory.
            let path = try load(url: NavigationManager.dataURL)
            self.path = path
        } catch {
            // Handle error
        }
    }
    
    func save() {
        guard let codableRepresentation = path.codable else { return }
        let encoder = JSONEncoder()
        do {
            let data = try encoder.encode(codableRepresentation)
            try data.write(to: NavigationManager.dataURL)
        } catch {
            //Handle error.
        }
    }
    
    /// Load the navigation path from a previously saved data.
    func load(url: URL) throws -> NavigationPath {
        let data = try Data(contentsOf: url, options: .mappedIfSafe)
        let decoder = JSONDecoder()
        let path = try decoder.decode(NavigationPath.CodableRepresentation.self, from: data)
        return NavigationPath(path)
    }
}

```

In the example above, the `save` method checks `path.codable` for nullability. This value describes the contents of the path in a serializable format. It returns `nil` if any of the type-erased elements of the path don’t conform to the `codable`.

It’s important to perform this check because `NavigationPath` doesn’t require the data types to conform to `Codable`. `NavigationPath` only needs the types to conform to `Hashable`, and as a result, you can’t verify that the navigation path is a valid representation of `Codable` at compile time.

To learn more about navigation stacks, links and paths, see [`Bringing robust navigation structure to your SwiftUI app`](bringing-robust-navigation-structure-to-your-swiftui-app.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/SwiftUI/understanding-the-composition-of-navigation-stack)*