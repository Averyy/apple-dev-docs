# padding(toLength:withPad:startingAt:)

**Framework**: Foundation  
**Kind**: method

Returns a new string formed from the receiver by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.

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
func padding(toLength newLength: Int, withPad padString: String, startingAt padIndex: Int) -> String
```

#### Return Value

A new string formed from the receiver by either removing characters from the end, or by appending as many occurrences of `padString` as necessary.

#### Discussion

Here are some examples of usage:

```objc
[@"abc" stringByPaddingToLength: 9 withString: @"." startingAtIndex:0];
    // Results in "abc......"
 
[@"abc" stringByPaddingToLength: 2 withString: @"." startingAtIndex:0];
    // Results in "ab"
 
[@"abc" stringByPaddingToLength: 9 withString: @". " startingAtIndex:1];
    // Results in "abc . . ."
    // Notice that the first character in the padding is " "
```

## Parameters

- `newLength`: The new length for the receiver.
- `padString`: The string with which to extend the receiver.
- `padIndex`: The index in   from which to start padding.

## See Also

- [func appendingFormat(NSString, any CVarArg...) -> NSString](nsstring/appendingformat(_:_:).md)
- [func appending(String) -> String](nsstring/appending(_:).md)
  Returns a new string made by appending a given string to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/padding(tolength:withpad:startingat:))*