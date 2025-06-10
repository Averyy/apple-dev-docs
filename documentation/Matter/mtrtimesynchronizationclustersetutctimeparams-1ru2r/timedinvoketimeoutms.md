# timedInvokeTimeoutMs

**Framework**: Matter  
**Kind**: property

Controls whether the command is a timed command (using Timed Invoke).

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.0+
- watchOS 10.2+

## Declaration

```swift
@NSCopying
var timedInvokeTimeoutMs: NSNumber? { get set }
```

#### Discussion

If nil (the default value), a regular invoke is done for commands that do not require a timed invoke and a timed invoke with some default timed request timeout is done for commands that require a timed invoke.

If not nil, a timed invoke is done, with the provided value used as the timed request timeout.  The value should be chosen small enough to provide the desired security properties but large enough that it will allow a round-trip from the sever to the client (for the status response and actual invoke request) within the timeout window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclustersetutctimeparams-1ru2r/timedinvoketimeoutms)*