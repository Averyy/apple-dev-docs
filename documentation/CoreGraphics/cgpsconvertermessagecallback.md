# CGPSConverterMessageCallback

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

Passes messages generated during a PostScript conversion process.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
typealias CGPSConverterMessageCallback = (UnsafeMutableRawPointer?, CFString) -> Void
```

```c
typedef void (*)(void *, const struct __CFString *) CGPSConverterMessageCallback;
```

#### Discussion

There are several kinds of message that might be sent during a conversion process. The most likely are font substitution messages, and any messages that the PostScript code itself generates. Any PostScript messages written to `stdout` are routed through this callback—typically these are debugging or status messages and, although uncommon, can be useful in debugging. In addition, there may be error messages if the document is malformed.

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [`init(info:callbacks:options:)`](./cgpsconverter/init%28info,callbacks,options%29.md).
- `message`: A string containing the message from the PostScript conversion process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconvertermessagecallback)*