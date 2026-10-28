# musicPicker(isPresented:title:selection:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a music picker to select items from the Apple Music catalog and the user’s music library.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency func musicPicker<Selection>(isPresented: Binding<Bool>, title: Text? = nil, selection: Binding<Selection?>) -> some View where Selection : PickableMusicItem
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func musicPicker<Selection>(isPresented: Binding<Bool>, title: Text? = nil, selection: Binding<MusicItemCollection<Selection>>) -> some View where Selection : PickableMusicItem
```

```swift
@MainActor
@preconcurrency func musicPicker<Selection>(isPresented: Binding<Bool>, title: Text? = nil, selection: Binding<[Selection]>) -> some View where Selection : PickableMusicItem
```

## Discussion

Example:

```swift
struct MusicPickerButton: View {
    @State private var isShowingMusicPicker = false
    @State private var selectedSong: Song?

    var body: some View {
        Button("Pick a song") {
            isShowingMusicPicker = true
        }
        .musicPicker(isPresented: $isShowingMusicPicker, selection: $selectedSong)
    }
}
```

## Parameters

- `isPresented`: The binding to whether the music picker should be shown.
- `title`: The title to be shown in the navigation bar.
- `selection`: The selected music item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/musicpicker(ispresented:title:selection:)-61a8e)*