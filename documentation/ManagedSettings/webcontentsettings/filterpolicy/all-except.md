# WebContentSettings.FilterPolicy.all(except:)

**Framework**: ManagedSettings  
**Kind**: case

The system blocks all websites except the ones you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case all(except: Set<WebDomain> = [])
```

#### Discussion

Your app can specify up to 50 web domains exceptions.

## See Also

- [case auto(Set<WebDomain>, except: Set<WebDomain>)](webcontentsettings/filterpolicy/auto(_:except:).md)
  The system blocks adult content.
- [WebContentSettings.FilterPolicy.none](webcontentsettings/filterpolicy/none.md)
  The policy doesn’t affect any domains.
- [WebContentSettings.FilterPolicy.specific(_:)](webcontentsettings/filterpolicy/specific(_:).md)
  The policy blocks the specified domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webcontentsettings/filterpolicy/all(except:))*