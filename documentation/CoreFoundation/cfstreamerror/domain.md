# domain

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

The error domain that should be used to interpret the error. See [`CFStreamErrorDomain`](../cfstreamerrordomain.md) for possible values.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

> **Deprecated**: Use [`CFReadStreamCopyError(_:)`](../cfreadstreamcopyerror%28_%29.md) and [`CFWriteStreamCopyError(_:)`](../cfwritestreamcopyerror%28_%29.md) instead.

## Declaration

```swift
var domain: CFIndex
```

```c
CFIndex domain;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamerror/domain)*