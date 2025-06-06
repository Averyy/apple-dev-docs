# string(from:)

**Framework**: Foundation  
**Kind**: method

Creates a formatted string for an array of items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func string(from items: [Any]) -> String?
```

#### Return Value

A formatted string representing the list of objects in an array. Returns `nil` if the formatter can’t generate a description for all objects in the array, or if `obj` is `nil`.

#### Discussion

The list formatter uses [`itemFormatter`](listformatter/itemformatter.md) to format each item in the array. If [`itemFormatter`](listformatter/itemformatter.md) doesn’t apply to a particular item, the list formatter falls back to the item’s [`description(withLocale:)`](nsarray/description(withlocale:).md) or [`localizedDescription`](progress/localizeddescription.md) if implemented. If those methods aren’t implemented, the formatter uses [`description`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/description) instead.

## Parameters

- `items`: An array of objects to format as a list.

## See Also

- [func string(for: Any?) -> String?](listformatter/string(for:).md)
  Creates a formatted string for an array of items.
- [class func localizedString(byJoining: [String]) -> String](listformatter/localizedstring(byjoining:).md)
  Constructs a formatted string from an array of strings that uses the list format specific to the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatter/string(from:))*