# string(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSString *) stringFromItems:(NSArray *) items;
```

#### Return Value

A formatted string representing the list of objects in an array. Returns `nil` if the formatter can’t generate a description for all objects in the array, or if `obj` is `nil`.

#### Discussion

The list formatter uses [`itemFormatter`](./itemformatter.md) to format each item in the array. If [`itemFormatter`](./itemformatter.md) doesn’t apply to a particular item, the list formatter falls back to the item’s [`description(withLocale:)`](../nsarray/description%28withlocale%29.md) or [`localizedDescription`](../progress/localizeddescription.md) if implemented. If those methods aren’t implemented, the formatter uses [`description`](../../ObjectiveC/nsobjectprotocol/description.md) instead.

## Parameters

- `items`: An array of objects to format as a list.

## See Also

### Converting Arrays to Formatted Lists
- [func string(for: Any?) -> String?](./string%28for%29.md)
  Creates a formatted string for an array of items.
- [class func localizedString(byJoining: [String]) -> String](./localizedstring%28byjoining%29.md)
  Constructs a formatted string from an array of strings that uses the list format specific to the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatter/string(from:))*