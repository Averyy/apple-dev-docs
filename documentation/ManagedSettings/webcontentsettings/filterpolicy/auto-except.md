# WebContentSettings.FilterPolicy.auto(_:except:)

**Framework**: ManagedSettings  
**Kind**: case

The system blocks adult content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case auto(Set<WebDomain> = [], except: Set<WebDomain> = [])
```

#### Discussion

The system also blocks websites you provide in `domains`. The system allows websites you provide in `except`, overriding the adult content filter and `domains` set. Your app can block up to 50 web domains and specify up to 50 web domains exceptions at once.

## See Also

- [WebContentSettings.FilterPolicy.all(except:)](webcontentsettings/filterpolicy/all(except:).md)
  The system blocks all websites except the ones you specify.
- [WebContentSettings.FilterPolicy.none](webcontentsettings/filterpolicy/none.md)
  The policy doesn’t affect any domains.
- [WebContentSettings.FilterPolicy.specific(_:)](webcontentsettings/filterpolicy/specific(_:).md)
  The policy blocks the specified domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webcontentsettings/filterpolicy/auto(_:except:))*