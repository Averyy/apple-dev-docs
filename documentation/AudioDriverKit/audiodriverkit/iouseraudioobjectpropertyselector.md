# IOUserAudioObjectPropertySelector

**Framework**: AudioDriverKit  
**Kind**: typealias

A four character code which, along with the scope and element, specific piece of information about an audio object.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
typedef uint32_t IOUserAudioObjectPropertySelector;
```

#### Discussion

The property selector specifies the general classification of the property such as volume, stream format, or latency. Each class has a different set of selectors. A subclass inherits its superclass’s set of selectors, although it may not implement them all.

## See Also

- [PropertiesChanged](iouseraudiodriver/propertieschanged.md)
  Informs the host when the state of an object in the driver changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioobjectpropertyselector)*