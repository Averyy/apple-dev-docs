# copy(_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Applies the copy rule to a resource at the given path.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
static func copy(_ path: String) -> Resource
```

#### Return Value

A `Resource` instance.

#### Discussion

If possible, use [`process(_:localization:)`](./process%28_,localization%29.md) and automatically apply optimizations to resources.

If your resources must remain untouched or must retain a specific folder structure, use the `copy` rule. It copies resources at the given `path`, as is, to the top level in the package’s resource bundle. If the given path represents a directory, Swift Package Manager preserves its structure.

## Parameters

- `path`: The path for a resource.

## See Also

### Applying Rules
- [static func process(String, localization: Resource.Localization?) -> Resource](./process%28_,localization%29.md)
  Applies a platform-specific rules to the resource at the given path.
- [Resource.Localization](./localization.md)
  Defines the explicit type of localization for resources.
- [static func embedInCode(String) -> Resource](./embedincode%28_%29.md)
  Applies the embed rule to a resource at the given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/resource/copy(_:))*