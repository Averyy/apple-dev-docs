# UILaunchStoryboardDefinitions

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

An array of dictionaries mapping launch storyboard identifiers to storyboards.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+

## Details

- **Name**: `UILaunchStoryboardDefinitions`
- **Type**: array of dictionary 

#### Discussion

Each dictionary has [`UILaunchStoryboardFile`](./uilaunchstoryboarddefinitions/uilaunchstoryboardfile.md) and [`UILaunchStoryboardIdentifier`](./uilaunchstoryboarddefinitions/uilaunchstoryboardidentifier.md) keys, associating a storyboard file or xib with an identifier.

## Topics

### Specifying Storyboard Identifiers
- [UILaunchStoryboardIdentifier](./uilaunchstoryboarddefinitions/uilaunchstoryboardidentifier.md)
  A user-specified identifier for a launch storyboard.
- [UILaunchStoryboardFile](./uilaunchstoryboarddefinitions/uilaunchstoryboardfile.md)
  A launch storyboard file or xib.

## See Also

### Specifying Launch Storyboards
- [UIDefaultLaunchStoryboard](./uidefaultlaunchstoryboard.md)
  The identifier of the default launch storyboard to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchstoryboards/uilaunchstoryboarddefinitions)*