# identifier

**Framework**: Background Tasks  
**Kind**: property  
**Role**: Instance Property

The string identifier of the task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (copy, readonly) NSString * identifier;
```

#### Discussion

The identifier is the same as the one used to register the launch handler in [`register(forTaskWithIdentifier:using:launchHandler:)`](../bgtaskscheduler/register%28fortaskwithidentifier,using,launchhandler%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtask/identifier)*