# init(wrappedValue:_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can save and restore a `PersistentIdentifier`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
init(wrappedValue: Value, _ key: String) where Value == PersistentIdentifier
```

**Other overloads**:

```swift
init(wrappedValue: Value, _ key: String) where Value : RawRepresentable, Value.RawValue == Int
```

```swift
init(wrappedValue: Value, _ key: String) where Value : RawRepresentable, Value.RawValue == String
```

```swift
init(wrappedValue: Value, _ key: String) where Value == Bool
```

```swift
init(wrappedValue: Value, _ key: String) where Value == Data
```

```swift
init(wrappedValue: Value, _ key: String) where Value == Date
```

```swift
init(wrappedValue: Value, _ key: String) where Value == Double
```

```swift
init(wrappedValue: Value, _ key: String) where Value == Int
```

```swift
init(wrappedValue: Value, _ key: String) where Value == String
```

```swift
init(wrappedValue: Value, _ key: String) where Value == URL
```

```swift
init<RowValue>(wrappedValue: Value = TableColumnCustomization<RowValue>(), _ key: String) where Value == TableColumnCustomization<RowValue>, RowValue : Identifiable
```

## Discussion

```swift
@Model class Recipe { ... }
struct RecipeList: View {
    @Query var recipes: [Recipe]
    @SceneStorage("selectedID")
    var selectedRecipeID: Recipe.ID = RecipeStore.recipes[0].id

    var body: some View {
        List(recipes, selection: $selectedRecipeID) { recipe in
            RecipeDetail(recipe)
        }
    }
}
```

## Parameters

- `wrappedValue`: The default value when there is no saved value for the given key.
- `key`: A key used to save and restore the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenestorage/init(wrappedvalue:_:)-9eye6)*