# CGPSConverterMessageCallback

**Framework**: Core Graphics  
**Kind**: typealias

Passes messages generated during a PostScript conversion process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias CGPSConverterMessageCallback = (UnsafeMutableRawPointer?, CFString) -> Void
```

#### Discussion

There are several kinds of message that might be sent during a conversion process. The most likely are font substitution messages, and any messages that the PostScript code itself generates. Any PostScript messages written to `stdout` are routed through this callback—typically these are debugging or status messages and, although uncommon, can be useful in debugging. In addition, there may be error messages if the document is malformed.

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to  .
- `message`: A string containing the message from the PostScript conversion process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconvertermessagecallback)*