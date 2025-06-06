# platform

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The platform on which to run the provider.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency static var platform: PreviewPlatform? { get }
```

#### Discussion

Xcode infers the platform for a preview based on the currently selected target. If you have a multiplatform target and want to suggest a particular target for a preview, implement the `platform` computed property to provide a hint, and specify one of the [`PreviewPlatform`](previewplatform.md) values:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
    }

    static var platform: PreviewPlatform? {
        PreviewPlatform.tvOS
    }
}
```

Xcode ignores this value unless you have a multiplatform target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewprovider/platform)*