# typeSelectEquivalent(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Sets an explicit type select equivalent text in a collection, such as a list or table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func typeSelectEquivalent(_ stringResource: LocalizedStringResource) -> some View
```

#### Discussion

By default, a type select equivalent is automatically derived from any `Text` or `TextField` content in a list or table. In the below example, type select can be used to select a person, even though no explicit value has been set.

```None
List(people, selection: $selectedPersonID) { person in
    Label {
        Text(person.name)
    } icon: {
        person.avatar
    }
}
```

An explicit type select value should be set when there is no textual content or when a different value is desired compared to what’s displayed in the view. Explicit values also provide a more performant for complex view types. In the below example, type select is explicitly set to allow selection of views that otherwise only display an image.

```None
List(people, selection: $selectedPersonID) { person in
    person.avatar
        .accessibilityLabel(person.name)
        .typeSelectEquivalent(person.name)
}
```

Setting an empty string value disables text selection for the view, and a value of `nil` results in the view using its default value.

## Parameters

- `stringResource`: The localized string resource to use as a   type select equivalent for a view in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/typeselectequivalent(_:)-2k5ll)*