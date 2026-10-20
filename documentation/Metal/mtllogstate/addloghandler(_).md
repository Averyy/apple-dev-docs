# addLogHandler(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds a log handler to customize the presentation of shader logging.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func addLogHandler(_ block: @escaping @Sendable (String?, String?, MTLLogLevel, String) -> Void)
```

```objc
- (void) addLogHandler:(void (^)(NSString *subSystem, NSString *category, MTLLogLevel logLevel, NSString *message)) block;
```

## Mentions

- [Logging shader debug messages](../logging-shader-debug-messages.md)

#### Discussion

In absence of any log handlers, all messages goes through the unified log system and are available through the console.app, log tool, or Xcode.

Use this method to add your own shader logging presentation or filter messages using subsystem, category and levels. For more details on how to configure your logging, see [Generating Log Messages from Your Code](../../os/generating-log-messages-from-your-code.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllogstate/addloghandler(_:))*