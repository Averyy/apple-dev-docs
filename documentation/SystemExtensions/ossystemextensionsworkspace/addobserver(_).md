# addObserver(_:)

**Framework**: System Extensions  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 15.1+

## Declaration

```swift
func addObserver(_ observer: any OSSystemExtensionsWorkspaceObserver) throws
```

```objc
- (BOOL) addObserver:(id<OSSystemExtensionsWorkspaceObserver>) observer error:(NSError **) error;
```

## Discussion

Start observing changes to System Extension(s) which are enabled or ready to be enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionsworkspace/addobserver(_:))*