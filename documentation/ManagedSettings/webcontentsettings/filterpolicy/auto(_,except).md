# WebContentSettings.FilterPolicy.auto(_:except:)

**Framework**: Managed Settings  
**Kind**: case  
**Role**: Case

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

### Providing filters and exceptions
- [WebContentSettings.FilterPolicy.all(except:)](./all%28except%29.md)
  The system blocks all websites except the ones you specify.
- [WebContentSettings.FilterPolicy.none](./none.md)
  The policy doesn’t affect any domains.
- [WebContentSettings.FilterPolicy.specific(_:)](./specific%28_%29.md)
  The policy blocks the specified domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webcontentsettings/filterpolicy/auto(_:except:))*