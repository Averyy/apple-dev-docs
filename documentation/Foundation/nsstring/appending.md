# appending(_:)

**Framework**: Foundation  
**Kind**: method

Returns a new string made by appending a given string to the receiver.

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
func appending(_ aString: String) -> String
```

#### Return Value

A new string made by appending `aString` to the receiver.

#### Discussion

This code excerpt, for example:

```objc
NSString *errorTag = @"Error: ";
NSString *errorString = @"premature end of file.";
NSString *errorMessage = [errorTag stringByAppendingString:errorString];
```

produces the string “`Error: premature end of file.`”.

## Parameters

- `aString`: The string to append to the receiver. This value must not be  .

## See Also

- [func appendingFormat(NSString, any CVarArg...) -> NSString](nsstring/appendingformat(_:_:).md)
- [func padding(toLength: Int, withPad: String, startingAt: Int) -> String](nsstring/padding(tolength:withpad:startingat:).md)
  Returns a new string formed from the receiver by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/appending(_:))*