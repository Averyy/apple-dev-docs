# description(withLocale:indent:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a string that represents the contents of the array, formatted as a property list.

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
func description(withLocale locale: Any?, indent level: Int) -> String
```

```objc
- (NSString *) descriptionWithLocale:(id) locale indent:(NSUInteger) level;
```

## Return Value

A string that represents the contents of the array, formatted as a property list.

## Discussion

The returned `NSString` object contains the string representations of each of the array’s elements, in order, from first to last. To obtain the string representation of a given element, [`description(withLocale:indent:)`](./description%28withlocale,indent%29.md) proceeds as follows:

- If the element is an `NSString` object, it is used as is.
- If the element responds to [`description(withLocale:indent:)`](./description%28withlocale,indent%29.md), that method is invoked to obtain the element’s string representation.
- If the element responds to [`description(withLocale:)`](./description%28withlocale%29.md), that method is invoked to obtain the element’s string representation.
- If none of the above conditions is met, the element’s string representation is obtained by invoking its [`description`](./description.md) method.

## Parameters

- `locale`: An `NSLocale` object or an `NSDictionary` object that specifies options used for formatting each of the array’s elements (where recognized). Specify `nil` if you don’t want the elements formatted.
- `level`: A level of indent, to make the output more readable: set `level` to `0` to use four spaces to indent, or `1` to indent the output with a tab character.

## See Also

### Creating a Description
- [var description: String](./description.md)
  A string that represents the contents of the array, formatted as a property list.
- [func description(withLocale: Any?) -> String](./description%28withlocale%29.md)
  Returns a string that represents the contents of the array, formatted as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/description(withlocale:indent:))*