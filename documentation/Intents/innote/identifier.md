# identifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique identifier that you use to identify the note internally.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INNote is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var identifier: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * identifier;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * identifier;
```

#### Discussion

Use this value internally to locate notes in your app’s data structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innote/identifier)*