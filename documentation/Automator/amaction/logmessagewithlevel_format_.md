# logMessageWithLevel:format:

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Displays a message in Automator’s log area.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.7+

## Declaration

```objc
- (void) logMessageWithLevel:(AMLogLevel) level format:(NSString *) format;
```

#### Discussion

This message is visible to the user. Use this method if you wish to provide feedback to the user in Automator’s log area as your action runs.

## Parameters

- `level`: The level of logging to perform. See [`AMLogLevel`](../amloglevel.md) for possible values.
- `format`: A format string. See [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) for examples of how to use this method, and [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265) for a list of format specifiers.

## See Also

### Performing Logging
- [enum AMLogLevel](../amloglevel.md)
  Logging levels that Automator supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/logmessagewithlevel:format:)*