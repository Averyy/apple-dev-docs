# INGetVisualCodeIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request for a visual code to use for exchanging payment and contact information.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INGetVisualCodeIntent
```

```objc
@interface INGetVisualCodeIntent : INIntent
```

## Overview

Siri creates an [`INGetVisualCodeIntent`](./ingetvisualcodeintent.md) object when the user asks for a visual code to use with a scanner. A visual code is a bar code or QR code that embeds information about a transaction. For example, an app might provide a visual code to facilitate payment for services. Apps can also use visual codes to communicate a user’s contact information.

To handle this intent, the handler object in your Intents extension must adopt the [`INGetVisualCodeIntentHandling`](./ingetvisualcodeintenthandling.md) protocol. Your handler should confirm the request and create an [`INGetVisualCodeIntentResponse`](./ingetvisualcodeintentresponse.md) object with an image containing the visual code. Siri handles the display of the provided visual code in order to scan it.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Suggestions |
| Always requires unlocked device | Yes |

When performing a search, Siri automatically asks the user to unlock a currently locked device. You don’t need to explicitly ask to unlock the device. In addition, Siri always prompts the user to confirm the request before asking your Intents extension to handle it.

### Example Phrases

Users can ask Siri to display visual codes in a variety of ways. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Show my personal QR code | Display my payment code |
| zh_CN | 显示我的个人二维码 | 显示我的支付码 |
| zh_HK | 顯示我嘅二維碼 | 顯示我嘅支付碼 |
| zh_TW | 顯示我的通訊錄二維碼 | 顯示我的支付二維碼 |
| yue_CN | 显示我嘅二维码 | 显示我嘅支付码 |
| ar | أرني رمز QR الخاص بي | اعرض رمز الدفع الخاص بي |
| da | vis min qr kode | vis min betalings kode |
| de | Zeige meinen persönlichen QR-Code | Zeige meinen Zahlungscode |
| es | Muestra mi código QR | Muestra mi código de pago |
| fi | Näytä oma QR-koodini | Näytä maksukoodini |
| fr | Montre-moi mon code QR personnel | Affiche mon code de paiement |
| he | תראי את הקוד QR הפרטי שלי | תראי את הקוד תשלום שלי |
| it | Mostrami il mio codice QR personale | Mostra il mio codice di pagamento |
| ja | 自分のQRコードを表示 | 自分の支払いコードを表示 |
| ko | 나의 개인 QR 코드 보여줘 | 나의 결제 코드 보여줘 |
| ms | Tunjukkan kod QR peribadi saya | Paparkan kod bayaran saya |
| nb | Vis min personlige QR-kode | Vis betalingskoden min |
| nl | Toon mijn persoonlijke QR-code | Geef mijn betalingscode weer |
| pt | Mostre meu código QR pessoal | Mostra meu código QR de pagamento |
| ru | Покажи мой личный QR-код | Отобрази мой код оплаты |
| sv | Visa min QR-kod | Visa min betalkod |
| th | โชว์คิวอาร์โค้ดของฉัน | แสดงโค้ดการจ่ายเงินของฉัน |
| tr | QR kodumu göster | Ödeme kodumu görüntüle |

## Topics

### Initializing the Intent Object
- [init(visualCodeType: INVisualCodeType)](./ingetvisualcodeintent/init%28visualcodetype%29.md)
  Initializes the intent object with information about the requested type of code.
### Getting the Visual Code Type
- [var visualCodeType: INVisualCodeType](./ingetvisualcodeintent/visualcodetype.md)
  The type of visual code requested by the user.
- [enum INVisualCodeType](./invisualcodetype.md)
  Constants indicating the purpose of the visual code.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Visual Codes
- [protocol INGetVisualCodeIntentHandling](./ingetvisualcodeintenthandling.md)
  The handler interface for displaying your app’s visual codes.
- [class INGetVisualCodeIntentResponse](./ingetvisualcodeintentresponse.md)
  Your app’s response to a request for a visual code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetvisualcodeintent)*