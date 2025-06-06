# processInfo

**Framework**: Foundation  
**Kind**: property

Returns the process information agent for the process.

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
class var processInfo: ProcessInfo { get }
```

#### Return Value

Shared process information agent for the process.

#### Discussion

An [`ProcessInfo`](processinfo.md) object is created the first time this method is invoked, and that same object is returned on each subsequent invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/processinfo)*