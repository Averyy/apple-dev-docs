# appleEvent

**Framework**: Foundation  
**Kind**: property

If the receiver was constructed by Cocoa scripting’s built-in Apple event handling, returns the Apple event descriptor from which it was constructed.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
@NSCopying
var appleEvent: NSAppleEventDescriptor? { get }
```

#### Discussion

The effects of mutating or retaining this descriptor are undefined, although it may be copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/appleevent)*