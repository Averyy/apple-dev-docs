# init(_:traits:arguments:body:)

**Framework**: DeveloperToolsSupport  
**Kind**: init

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init<T>(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], @PreviewBodyBuilder<UIView> body: @escaping @MainActor (T) -> UIView)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:traits:arguments:body:)-3q0i9)*