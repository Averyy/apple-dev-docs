# objc_copyImageHeaders(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Returns the Mach headers of all the images loaded into the current process that contain Objective-C or Swift code.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
func objc_copyImageHeaders(_ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<OpaquePointer>
```

*Mac Catalyst, macOS*

```swift
func objc_copyImageHeaders(_ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<mach_header>>
```

```c
extern const struct mach_header **objc_copyImageHeaders(unsigned int *outCount);
```

#### Return Value

An array of @c mach_header pointers. The array contains @c *outCount pointers followed by a @c NULL terminator. You must free the array with

## Parameters

- `outCount`: The number of image headers returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_copyimageheaders(_:))*