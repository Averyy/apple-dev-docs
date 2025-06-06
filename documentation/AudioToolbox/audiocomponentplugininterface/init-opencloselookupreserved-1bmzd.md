# init(Open:Close:Lookup:reserved:)

**Framework**: Audio Toolbox  
**Kind**: init

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
init(Open: (UnsafeMutableRawPointer, AudioComponentInstance) -> OSStatus, Close: (UnsafeMutableRawPointer) -> OSStatus, Lookup: (Int16) -> AudioComponentMethod?, reserved: UnsafeMutableRawPointer?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface/init(open:close:lookup:reserved:)-1bmzd)*