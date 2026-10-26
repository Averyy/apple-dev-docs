# stringByAppendingFormat:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a string made by appending to the receiver a string constructed from a given format string and the following arguments.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (NSString *) stringByAppendingFormat:(NSString *) format;
```

#### Return Value

A string made by appending to the receiver a string constructed from `format` and the following arguments, in the manner of [`stringWithFormat:`](./stringwithformat_.md).

#### Discussion

Pass a comma-separated list of variadic arguments to substitute into `format`.

## Parameters

- `format`: A format string. See [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) for more information. This value must not be `nil`.

  > ❗ **Important**:  Raises an `NSInvalidArgumentException` if `format` is `nil`.

## See Also

### Combining Strings
- [func appending(String) -> String](./appending%28_%29.md)
  Returns a new string made by appending a given string to the receiver.
- [func padding(toLength: Int, withPad: String, startingAt: Int) -> String](./padding%28tolength,withpad,startingat%29.md)
  Returns a new string formed from the receiver by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/stringbyappendingformat:)*