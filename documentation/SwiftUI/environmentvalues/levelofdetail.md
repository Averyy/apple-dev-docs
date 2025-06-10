# levelOfDetail

**Framework**: SwiftUI  
**Kind**: property

The level of detail the view is recommended to have.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var levelOfDetail: LevelOfDetail { get set }
```

#### Discussion

Read from the environment with

```swift
@Environment(\.levelOfDetail) var levelOfDetail
```

To customize your view based on recommended level of detail, read the environment value using the `.levelOfDetail` key and apply that to change your view.

```swift
var body: some View {
     switch levelOfDetail {
     case .default:
         VStack {
            NewsTitleView()
            NewsBodyView()
         }
     case .simplified:
         NewsImageOverview()
     }
}
```

> **Note**: The levelOfDetail can be determined by different factors depending on the platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/levelofdetail)*