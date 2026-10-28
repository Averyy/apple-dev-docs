# process(_:localization:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Applies a platform-specific rules to the resource at the given path.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
static func process(_ path: String, localization: Resource.Localization? = nil) -> Resource
```

## Return Value

A `Resource` instance.

## Discussion

Use the `process` rule to process resources at the given path according to the platform Swift Package Manager builds the target for. For example, Swift Package Manager may optimize image files for platforms that support such optimizations. If no optimization is available for a file type, Swift Package Manager copies the file.

If the given path represents a directory, Swift Package Manager applies the process rule recursively to each file in the directory.

If possible, use this rule instead of [`copy(_:)`](./copy%28_%29.md).

## Parameters

- `path`: The path for a resource.
- `localization`: The explicit localization type for the resource.

## See Also

### Applying Rules
- [Resource.Localization](./localization.md)
  Defines the explicit type of localization for resources.
- [static func copy(String) -> Resource](./copy%28_%29.md)
  Applies the copy rule to a resource at the given path.
- [static func embedInCode(String) -> Resource](./embedincode%28_%29.md)
  Applies the embed rule to a resource at the given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/resource/process(_:localization:))*