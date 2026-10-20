# description(withLocale:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a string that represents the contents of the ordered set, formatted as a property list.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func description(withLocale locale: Any?) -> String
```

```objc
- (NSString *) descriptionWithLocale:(id) locale;
```

#### Return Value

A string that represents the contents of the ordered set, formatted as a property list.

#### Discussion

For a description of how locale is applied to each element in the receiving ordered set, see [`description(withLocale:indent:)`](./description%28withlocale,indent%29.md).

## Parameters

- `locale`: An [`NSLocale`](../nslocale.md) object or an `NSDictionary` object that specifies options used for formatting each of the ordered set’s elements (where recognized). Specify `nil` if you don’t want the elements formatted.

## See Also

### Describing a Set
- [var description: String](./description.md)
  A string that represents the contents of the ordered set, formatted as a property list.
- [func description(withLocale: Any?, indent: Int) -> String](./description%28withlocale,indent%29.md)
  Returns a string that represents the contents of the ordered set, formatted as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/description(withlocale:))*