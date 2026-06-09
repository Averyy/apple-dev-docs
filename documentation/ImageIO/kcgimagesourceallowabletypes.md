# kCGImageSourceAllowableTypes

**Framework**: Image I/O  
**Kind**: var

Option key for restricting which image formats can be decoded.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
let kCGImageSourceAllowableTypes: CFString
```

#### Discussion

The value is a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) containing [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) Uniform Type Identifiers (UTIs) of allowed image formats. When specified, ImageIO will only decode images whose format matches one of the entries in the allow list. If no matching reader is found, decoding fails.

Unknown format identifiers are ignored. If not specified, all supported ImageIO formats are allowed (default behavior). If process-wide format restrictions were set via [`CGImageSourceSetAllowableTypes(_:)`](cgimagesourcesetallowabletypes(_:).md), only formats allowed by both mechanisms are permitted.

See also [`System-declared uniform type identifiers`](https://developer.apple.com/documentation/UniformTypeIdentifiers/system-declared-uniform-type-identifiers).

#### Example

**Swift**:

```swift
let allowedTypes = ["public.jpeg" as CFString, "public.png" as CFString]
let options = [
    kCGImageSourceAllowableTypes: allowedTypes
] as CFDictionary
```

**Objective-C**:

```objc
NSArray *allowedTypes = @[@"public.jpeg", @"public.png"];
NSDictionary *options = @{
    (id)kCGImageSourceAllowableTypes: allowedTypes
};
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagesourceallowabletypes)*