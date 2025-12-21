# PKPaymentNetwork

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

A type that represents a payment method.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct PKPaymentNetwork
```

## Topics

### Payment networks
- [static let amex: PKPaymentNetwork](pkpaymentnetwork/amex.md)
  An American Express payment card.
- [static let bancomat: PKPaymentNetwork](pkpaymentnetwork/bancomat.md)
  A Bancomat payment card.
- [static let bancontact: PKPaymentNetwork](pkpaymentnetwork/bancontact.md)
  A Bancontact payment card.
- [static let bankAxept: PKPaymentNetwork](pkpaymentnetwork/bankaxept.md)
- [static let barcode: PKPaymentNetwork](pkpaymentnetwork/barcode.md)
  A QR code to use for payment.
- [static let carteBancaire: PKPaymentNetwork](pkpaymentnetwork/cartebancaire.md)
- [static let cartesBancaires: PKPaymentNetwork](pkpaymentnetwork/cartesbancaires.md)
  A Cartes Bancaires payment card.
- [static let chinaUnionPay: PKPaymentNetwork](pkpaymentnetwork/chinaunionpay.md)
  A China Union Pay payment card.
- [static let dankort: PKPaymentNetwork](pkpaymentnetwork/dankort.md)
  The Dankort payment card.
- [static let discover: PKPaymentNetwork](pkpaymentnetwork/discover.md)
  A Discover payment card.
- [static let eftpos: PKPaymentNetwork](pkpaymentnetwork/eftpos.md)
  The electronic funds transfer at point of sale (EFTPOS) payment method.
- [static let electron: PKPaymentNetwork](pkpaymentnetwork/electron.md)
  An Electron debit card.
- [static let elo: PKPaymentNetwork](pkpaymentnetwork/elo.md)
  The Elo payment card.
- [static let girocard: PKPaymentNetwork](pkpaymentnetwork/girocard.md)
  A Girocard payment method.
- [static let idCredit: PKPaymentNetwork](pkpaymentnetwork/idcredit.md)
  An iD payment card.
- [static let interac: PKPaymentNetwork](pkpaymentnetwork/interac.md)
  The Interac payment method.
- [static let JCB: PKPaymentNetwork](pkpaymentnetwork/jcb.md)
  A JCB payment card.
- [static let mada: PKPaymentNetwork](pkpaymentnetwork/mada.md)
  A mada payment card.
- [static let maestro: PKPaymentNetwork](pkpaymentnetwork/maestro.md)
  A Maestro payment card.
- [static let masterCard: PKPaymentNetwork](pkpaymentnetwork/mastercard.md)
  A Mastercard payment card.
- [static let meeza: PKPaymentNetwork](pkpaymentnetwork/meeza.md)
- [static let mir: PKPaymentNetwork](pkpaymentnetwork/mir.md)
  A Mir payment card.
- [static let nanaco: PKPaymentNetwork](pkpaymentnetwork/nanaco.md)
  A Nanaco payment card.
- [static let NAPAS: PKPaymentNetwork](pkpaymentnetwork/napas.md)
- [static let pagoBancomat: PKPaymentNetwork](pkpaymentnetwork/pagobancomat.md)
- [static let postFinance: PKPaymentNetwork](pkpaymentnetwork/postfinance.md)
  A PostFinance AG payment card.
- [static let privateLabel: PKPaymentNetwork](pkpaymentnetwork/privatelabel.md)
  Store credit and debit cards.
- [static let quicPay: PKPaymentNetwork](pkpaymentnetwork/quicpay.md)
  A QUICPay payment card.
- [static let suica: PKPaymentNetwork](pkpaymentnetwork/suica.md)
  A Suica payment card.
- [static let tmoney: PKPaymentNetwork](pkpaymentnetwork/tmoney.md)
  The TMoney card.
- [static let visa: PKPaymentNetwork](pkpaymentnetwork/visa.md)
  A Visa payment card.
- [static let vPay: PKPaymentNetwork](pkpaymentnetwork/vpay.md)
  A Visa V Pay payment card.
- [static let waon: PKPaymentNetwork](pkpaymentnetwork/waon.md)
  A WAON payment card.
- [static let carteBancaires: PKPaymentNetwork](pkpaymentnetwork/cartebancaires.md)
  A Cartes Bancaires payment card.
### Initializers
- [init(String)](pkpaymentnetwork/init(_:).md)
  Creates a new payment network structure with the raw value you provide.
- [init(rawValue: String)](pkpaymentnetwork/init(rawvalue:).md)
  Creates a new payment network structure with the string you provide.
### Type Properties
- [static let conecs: PKPaymentNetwork](pkpaymentnetwork/conecs.md)
- [static let himyan: PKPaymentNetwork](pkpaymentnetwork/himyan.md)
- [static let jaywan: PKPaymentNetwork](pkpaymentnetwork/jaywan.md)
- [static let myDebit: PKPaymentNetwork](pkpaymentnetwork/mydebit.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func availableNetworks() -> [PKPaymentNetwork]](pkpaymentrequest/availablenetworks.md)
  Returns the list of available payment methods that Apple Pay supports.
- [var supportedNetworks: [PKPaymentNetwork]](pkpaymentrequest/supportednetworks.md)
  The payment methods that you support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentnetwork)*