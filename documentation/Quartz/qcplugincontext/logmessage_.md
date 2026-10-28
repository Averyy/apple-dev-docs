# logMessage:

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Writes a message to the Quartz Composer log.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

## Declaration

```objc
- (void) logMessage:(NSString *) format;
```

## Discussion

This method is an alternative to using the functions [`NSLog(_:_:)`](../../Foundation/nslog%28_,_%29.md) or `printf`.

## Parameters

- `format`: The string to write to the log. The default location for the log is the standard output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugincontext/logmessage:)*