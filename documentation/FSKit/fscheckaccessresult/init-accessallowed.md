# init(accessAllowed:)

**Framework**: FSKit  
**Kind**: init

Creates a result for an access-checking operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(accessAllowed: Bool)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `accessAllowed`: A Boolean value indicating whether the file system grants the requested access to the item. Pass `true` (Swift) or `YES` (Obj-C) to allow access, `false` (Swift) or `NO` (Obj-C) to deny access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscheckaccessresult/init(accessallowed:))*