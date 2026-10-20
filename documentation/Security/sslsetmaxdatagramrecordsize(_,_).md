# SSLSetMaxDatagramRecordSize(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the maximum datagram record size allowed by the application for a given context.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLSetMaxDatagramRecordSize(_ dtlsContext: SSLContext, _ maxSize: Int) -> OSStatus
```

```c
OSStatus SSLSetMaxDatagramRecordSize(SSLContextRef dtlsContext, size_t maxSize);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

The size you indicate includes all Datagram Transport Layer Security (DTLS) headers.

You can specify a new value up to the maximum size of a UDP packet (which, in turn, is based on the underlying IP protocol).

## Parameters

- `dtlsContext`: The SSL context associated with the connection.
- `maxSize`: The length value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetmaxdatagramrecordsize(_:_:))*