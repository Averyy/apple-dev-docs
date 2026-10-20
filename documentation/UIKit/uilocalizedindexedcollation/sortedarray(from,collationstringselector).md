# sortedArray(from:collationStringSelector:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sorts the objects within a section by their localized titles.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func sortedArray(from array: [Any], collationStringSelector selector: Selector) -> [Any]
```

```objc
- (NSArray *) sortedArrayFromArray:(NSArray *) array collationStringSelector:(SEL) selector;
```

#### Return Value

A new array containing the sorted items from the original `array` parameter.

#### Discussion

The table-view controller creates the array of objects for a section (`array`) as part of iterating through its model objects with calls to the [`section(for:collationStringSelector:)`](./section%28for,collationstringselector%29.md) method. This method should be called on each local section array.

## Parameters

- `array`: An array containing the model objects for a section.
- `selector`: The selector of a method implemented by the objects in `array` that returns the string to use for sorting the objects. The method represented by the selector must take no arguments and return an [`NSString`](../../Foundation/nsstring.md) object. For example, you might specify the selector for a name property of the object.

## See Also

### Preparing the sections and section indexes
- [func section(for: Any, collationStringSelector: Selector) -> Int](./section%28for,collationstringselector%29.md)
  Returns an integer identifying the section in which a model object belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/sortedarray(from:collationstringselector:))*