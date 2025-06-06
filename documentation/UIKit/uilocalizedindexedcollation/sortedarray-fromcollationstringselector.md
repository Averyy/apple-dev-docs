# sortedArray(from:collationStringSelector:)

**Framework**: UIKit  
**Kind**: method

Sorts the objects within a section by their localized titles.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func sortedArray(from array: [Any], collationStringSelector selector: Selector) -> [Any]
```

#### Return Value

A new array containing the sorted items from the original `array` parameter.

#### Discussion

The table-view controller creates the array of objects for a section (`array`) as part of iterating through its model objects with calls to the [`section(for:collationStringSelector:)`](uilocalizedindexedcollation/section(for:collationstringselector:).md) method. This method should be called on each local section array.

## Parameters

- `array`: An array containing the model objects for a section.
- `selector`: The selector of a method implemented by the objects in   that returns the string to use for sorting the objects. The method represented by the selector must take no arguments and return an   object. For example, you might specify the selector for a name property of the object.

## See Also

- [func section(for: Any, collationStringSelector: Selector) -> Int](uilocalizedindexedcollation/section(for:collationstringselector:).md)
  Returns an integer identifying the section in which a model object belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/sortedarray(from:collationstringselector:))*