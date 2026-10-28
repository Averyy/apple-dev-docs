# init(_:store:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can read and write an Optional data user default via `PersistentIdentifier`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == PersistentIdentifier?
```

**Other overloads**:

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == Bool?
```

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == Data?
```

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == Date?
```

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == Double?
```

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == Int?
```

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == String?
```

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == URL?
```

```swift
init<R>(_ key: String, store: UserDefaults? = nil) where Value == R?, R : RawRepresentable, R.RawValue == Int
```

```swift
init<R>(_ key: String, store: UserDefaults? = nil) where Value == R?, R : RawRepresentable, R.RawValue == String
```

## Discussion

Defaults to `nil` if there is no restored value.

```swift
@Model class Recipe { ... }
struct RecipeList: View {
    @Query var recipes: [Recipe]
    @SceneStorage("selectedID") var selectedRecipeID: Recipe.ID?

    var body: some View {
        List(recipes, selection: $selectedRecipeID) { recipe in
            RecipeDetail(recipe)
        }
    }
}
```

## Parameters

- `key`: The key to read and write the value to in the user defaults store.
- `store`: The user defaults store to read and write to. A value of `nil` will use the user default store from the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/appstorage/init(_:store:)-9lku2)*