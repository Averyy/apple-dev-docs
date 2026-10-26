# padding(toLength:withPad:startingAt:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSString *) stringByPaddingToLength:(NSUInteger) newLength withString:(NSString *) padString startingAtIndex:(NSUInteger) padIndex;
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
- `padIndex`: The index in `padString` from which to start padding.

## See Also

### Combining Strings
- [func appendingFormat(NSString, any CVarArg...) -> NSString](./appendingformat%28_,_%29.md)
- [func appending(String) -> String](./appending%28_%29.md)
  Returns a new string made by appending a given string to the receiver.
- [- stringByAppendingFormat:](./stringbyappendingformat_.md)
  Returns a string made by appending to the receiver a string constructed from a given format string and the following arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/padding(tolength:withpad:startingat:))*