# init(name:subdirectory:locale:bundle:)

**Framework**: Foundation  
**Kind**: init

Creates a URL resource from the given bundle, name, and subdirectory, optionally specifying a locale.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(name: String, subdirectory: String? = nil, locale: Locale = .current, bundle: Bundle = .main)
```

## Parameters

- `name`: The name of the resource in the bundle. This should include both the resource name and its extension, to avoid confusion.
- `subdirectory`: The subdirectory, if any, of the resource.
- `locale`: The locale of the resource, as provided by the process that creates the resource. This defaults to  .
- `bundle`: The bundle containing the resource. This defaults to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresource/init(name:subdirectory:locale:bundle:))*