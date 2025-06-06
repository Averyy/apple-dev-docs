# init(configurationFileNamed:)

**Framework**: StoreKit Test  
**Kind**: init

Initializes the test session with the provided configuration file that you include in your application’s bundle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
convenience init(configurationFileNamed filename: String) throws
```

#### Discussion

Create a configuration file in Xcode by selecting File > New > File and choosing StoreKit Configuration File. By default, the filename is `Configuration.storekit`. You can include multiple configuration files in your project, but only one can be active at a time. StoreKit configuration files always have a .`storekit` file extension.

To return all settings in the test session to the states defined in this configuration file, call [`resetToDefaultState()`](sktestsession/resettodefaultstate().md).

## Parameters

- `filename`: A StoreKit configuration file that you include in your application’s bundle.

## See Also

- [init(contentsOf: URL) throws](sktestsession/init(contentsof:).md)
  Initializes the test session with a configuration file you provide through a URL.
- [func resetToDefaultState()](sktestsession/resettodefaultstate.md)
  Removes all property overrides and resets all test session settings to their default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/init(configurationfilenamed:))*