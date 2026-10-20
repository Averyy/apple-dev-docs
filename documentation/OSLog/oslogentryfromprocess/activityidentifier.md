# activityIdentifier

**Framework**: OSLog  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The activity identifier associated with the entry.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var activityIdentifier: os_activity_id_t { get }
```

```objc
@property (nonatomic, readonly) os_activity_id_t activityIdentifier;
```

## See Also

### Identifying the Process Source
- [var process: String](./process.md)
  The name of the process that made the entry.
- [var processIdentifier: pid_t](./processidentifier.md)
  The process identifier that made the entry.
- [var sender: String](./sender.md)
  The name of the binary image that made the entry.
- [var threadIdentifier: UInt64](./threadidentifier.md)
  The identifier of the thread that made the entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentryfromprocess/activityidentifier)*