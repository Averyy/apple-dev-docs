# embedInCode(_:)

**Framework**: PackageDescription  
**Kind**: method

Applies the embed rule to a resource at the given path.

**Availability**:
- SwiftPM 5.9+

## Declaration

```swift
static func embedInCode(_ path: String) -> Resource
```

#### Return Value

A `Resource` instance.

#### Discussion

You can use the embed rule to embed the contents of the resource into the executable code.

## Parameters

- `path`: The path for a resource.

## See Also

- [static func process(String, localization: Resource.Localization?) -> Resource](resource/process(_:localization:).md)
  Applies a platform-specific rules to the resource at the given path.
- [Resource.Localization](resource/localization.md)
  Defines the explicit type of localization for resources.
- [static func copy(String) -> Resource](resource/copy(_:).md)
  Applies the copy rule to a resource at the given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/resource/embedincode(_:))*