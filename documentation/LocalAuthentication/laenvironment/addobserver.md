# addObserver(_:)

**Framework**: Local Authentication  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func addObserver(_ observer: any LAEnvironment.Observer)
```

#### Discussion

Adds observer to monitor changes of the environment.

The observer will be held weakly so its instance should be kept alive by the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/addobserver(_:))*