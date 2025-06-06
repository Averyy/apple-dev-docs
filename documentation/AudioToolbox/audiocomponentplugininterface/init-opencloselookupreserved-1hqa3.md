# init(Open:Close:Lookup:reserved:)

**Framework**: Audio Toolbox  
**Kind**: init

**Availability**:
- macOS ?+

## Declaration

```swift
init(Open: (UnsafeMutableRawPointer, AudioComponentInstance) -> OSStatus, Close: (UnsafeMutableRawPointer) -> OSStatus, Lookup: (Int16) -> AudioComponentMethod?, reserved: UnsafeMutableRawPointer?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface/init(open:close:lookup:reserved:)-1hqa3)*