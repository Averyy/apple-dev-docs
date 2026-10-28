# SSLGetDatagramWriteSize(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Provides the largest packet that the OS guarantees it can send without fragmentation.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLGetDatagramWriteSize(_ dtlsContext: SSLContext, _ bufSize: UnsafeMutablePointer<Int>) -> OSStatus
```

```c
OSStatus SSLGetDatagramWriteSize(SSLContextRef dtlsContext, size_t *bufSize);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

Although any packet below this threshold size will not be fragmented by the OS when sent using [`SSLWrite(_:_:_:_:)`](./sslwrite%28_,_,_,_%29.md), this function provides no guarantees about whether the packet will be fragmented by routers en route. This size value is equal to the maximum Datagram Record size (set by calling [`SSLSetMaxDatagramRecordSize(_:_:)`](./sslsetmaxdatagramrecordsize%28_,_%29.md)) minus the DTLS Record header size.

## Parameters

- `dtlsContext`: The SSL context associated with the connection.
- `bufSize`: The address of a `size_t` integer for storing the length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetdatagramwritesize(_:_:))*