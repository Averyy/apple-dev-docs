# processIdentifier

**Framework**: OSLog  
**Kind**: property  
**Required**: Yes

The process identifier that made the entry.

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
var processIdentifier: pid_t { get }
```

## See Also

- [var activityIdentifier: os_activity_id_t](oslogentryfromprocess/activityidentifier.md)
  The activity identifier associated with the entry.
- [var process: String](oslogentryfromprocess/process.md)
  The name of the process that made the entry.
- [var sender: String](oslogentryfromprocess/sender.md)
  The name of the binary image that made the entry.
- [var threadIdentifier: UInt64](oslogentryfromprocess/threadidentifier.md)
  The identifier of the thread that made the entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentryfromprocess/processidentifier)*