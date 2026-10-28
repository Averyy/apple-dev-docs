# CMBufferQueueGetTypeID()

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the type identifier of buffer queue objects.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMBufferQueueGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CMBufferQueueGetTypeID();
```

## Return Value

CFTypeID of `CMBufferQueue` objects.

## Discussion

You can check if a `CFTypeRef` object is actually a `CMBufferQueue` by comparing [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md)(object) with [`CMBufferQueueGetTypeID()`](./cmbufferqueuegettypeid%28%29.md)().


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuegettypeid())*